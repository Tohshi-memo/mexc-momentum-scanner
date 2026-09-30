# Decision Report

- generated_at: 2026-09-30T09:16:30.242827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15825**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15825, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.11% | **+0.08%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.29% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.08% | **+0.48%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.67% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,221.11** / 初期 $100.00 (+1121.11%)
- 確定: 5988件 (Win 1766 / Loss 1926 / Flat 2296) / skip 6398件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,221.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3536件 (Win 974 / Loss 812 / Flat 1750) / skip 5700件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3987件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-30T09:16:16.324314+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=83250.0
- Funnel: target 1079 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +86.94% | $7,654,540.95 |
| MOVR/USDT:USDT | +82.06% | $2,020,378.10 |
| AKE/USDT:USDT | +24.04% | $4,760,967.66 |
| PHA/USDT:USDT | +23.55% | $4,812,542.69 |
| SOONNETWORK/USDT:USDT | +14.85% | $5,351,571.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +1.69% | +1.42% |
| GRASS/USDT:USDT | below_1h_threshold | +1.43% | +1.16% |
| SOXS/USDT:USDT | below_1h_threshold | +1.39% | +1.12% |
| DOT/USDT:USDT | below_1h_threshold | +1.36% | +1.09% |
| INJ/USDT:USDT | below_1h_threshold | +1.02% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
