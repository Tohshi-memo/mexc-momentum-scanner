# Decision Report

- generated_at: 2026-11-06T13:06:25.468365+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18283**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18283, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_6PCT | 3/20 | 15.0% | +4.04% | **+0.61%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_BB3S | 5/18 | 27.8% | +1.31% | **+0.36%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.33% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.16% | **+1.95%** |
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.61% | **+1.70%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.89% | **+1.44%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.01% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7809件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$382.28** / 初期 $100.00 (+282.28%)
- 確定: 4653件 (Win 1250 / Loss 1034 / Flat 2369) / skip 7041件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1269 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $382.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6444件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T13:06:12.630877+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=75939.1
- Funnel: target 1089 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +117.24% | $14,511,720.62 |
| AKE/USDT:USDT | +99.53% | $38,758,309.13 |
| CYBER/USDT:USDT | +61.30% | $5,662,850.03 |
| ONE/USDT:USDT | +40.96% | $2,827,611.04 |
| JCT/USDT:USDT | +29.79% | $6,515,938.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.24% | +2.33% |
| UAI/USDT:USDT | below_1h_threshold | +2.10% | +2.19% |
| BIRB/USDT:USDT | below_1h_threshold | +2.03% | +2.12% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +1.78% | +1.87% |
| UVXY/USDT:USDT | below_1h_threshold | +1.55% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
