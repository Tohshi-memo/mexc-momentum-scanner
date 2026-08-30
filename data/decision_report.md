# Decision Report

- generated_at: 2026-08-30T00:41:22.162546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12981**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12981, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.35% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.51% | **+2.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.82% | **+2.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.93% | **+1.90%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.79% | **+1.39%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.75% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$787.12** / 初期 $100.00 (+687.12%)
- 確定: 4751件 (Win 1448 / Loss 1559 / Flat 1744) / skip 4791件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $787.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.68** / 初期 $100.00 (+72.68%)
- 確定: 2065件 (Win 575 / Loss 495 / Flat 995) / skip 4327件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2137 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $172.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2419件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000585 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-30T00:41:11.931640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78206.6
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 85.1 >= 65=1, 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +44.98% | $1,355,352.69 |
| PONS/USDT:USDT | +27.55% | $1,226,869.62 |
| PROM/USDT:USDT | +26.01% | $10,576,492.29 |
| BTR/USDT:USDT | +20.72% | $9,981,809.15 |
| HNT/USDT:USDT | +15.40% | $24,079,556.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +4.43% | +4.42% |
| BTR/USDT:USDT | below_1h_threshold | +2.75% | +2.74% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.26% | +2.25% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.23% | +1.23% |
| BEAT/USDT:USDT | below_1h_threshold | +1.03% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
