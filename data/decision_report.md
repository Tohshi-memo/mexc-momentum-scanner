# Decision Report

- generated_at: 2026-09-28T13:06:23.551773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15722**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15722, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.01% | **-2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_BB3S | 3/14 | 21.4% | +1.06% | **+0.23%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.07% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.32% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.41% | **+2.41%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.21% | **+1.32%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.39% | **+1.20%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +2.54% | **+1.01%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6301件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5599件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0221 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 3288件 (Win 953 / Loss 1288 / Flat 1047) / pending 6件 / skip 3903件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-09-28T13:06:12.404615+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=83351.1
- Funnel: target 1064 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +42.73% | $1,512,728.24 |
| QNT/USDT:USDT | +30.35% | $322,187,879.33 |
| MARSCOIN/USDT:USDT | +27.97% | $2,897,353.96 |
| HBAR/USDT:USDT | +27.45% | $90,524,484.82 |
| GRT/USDT:USDT | +13.70% | $13,566,910.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +0.89% | +1.12% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.68% | +0.92% |
| POL/USDT:USDT | below_1h_threshold | +0.67% | +0.90% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.43% | +0.67% |
| NAS100/USDT:USDT | below_1h_threshold | +0.33% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
