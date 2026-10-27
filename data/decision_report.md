# Decision Report

- generated_at: 2026-10-27T21:56:22.564982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17643**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17643, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +4.98% | **+1.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.17% | **+1.43%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.09% | **+0.93%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,579.72** / 初期 $100.00 (+1479.72%)
- 確定: 6751件 (Win 1968 / Loss 2164 / Flat 2619) / skip 7453件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,579.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$347.57** / 初期 $100.00 (+247.57%)
- 確定: 4172件 (Win 1139 / Loss 964 / Flat 2069) / skip 6882件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1271 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $347.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5806件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T21:56:13.083470+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80947.8
- Funnel: target 1083 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +36.96% | $2,263,811.20 |
| APR/USDT:USDT | +17.09% | $4,596,647.92 |
| BTW/USDT:USDT | +15.69% | $14,309,742.16 |
| BULLA/USDT:USDT | +8.11% | $10,536,612.18 |
| HAEDAL/USDT:USDT | +7.33% | $1,094,912.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HAEDAL/USDT:USDT | below_1h_threshold | +3.25% | +3.01% |
| DOOD/USDT:USDT | below_1h_threshold | +2.98% | +2.74% |
| APR/USDT:USDT | below_1h_threshold | +2.68% | +2.44% |
| IRYS/USDT:USDT | below_1h_threshold | +2.61% | +2.37% |
| CT/USDT:USDT | below_1h_threshold | +2.47% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
