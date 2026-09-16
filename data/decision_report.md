# Decision Report

- generated_at: 2026-09-16T12:11:29.763714+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14689**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14689, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.80% | **-1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.67% | **+0.67%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_5PCT | 13/20 | 65.0% | -0.03% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.81% | **+2.53%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.49% | **+2.37%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.15% | **+2.36%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +4.28% | **+1.90%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.12% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,149.40** / 初期 $100.00 (+1049.40%)
- 確定: 5566件 (Win 1666 / Loss 1798 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,149.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$238.03** / 初期 $100.00 (+138.03%)
- 確定: 3093件 (Win 855 / Loss 729 / Flat 1509) / skip 5007件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1779 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $238.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3206件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T12:11:12.659598+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=76095.4
- Funnel: target 1058 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1, 4h RSI 80.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +159.92% | $20,506,652.63 |
| BR/USDT:USDT | +103.15% | $24,156,431.54 |
| BULLA/USDT:USDT | +77.54% | $1,992,731.50 |
| LSK/USDT:USDT | +52.44% | $25,794,458.71 |
| 4/USDT:USDT | +15.54% | $1,563,795.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.47% | +1.62% |
| BTW/USDT:USDT | below_1h_threshold | +1.19% | +1.34% |
| KORU/USDT:USDT | below_1h_threshold | +1.14% | +1.29% |
| SNXX/USDT:USDT | below_1h_threshold | +1.03% | +1.19% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.99% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
