# Decision Report

- generated_at: 2026-11-01T17:11:20.131448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17980**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17980, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.73% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.80% | **+1.26%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.39% | **+1.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.63% | **+1.06%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,478.02** / 初期 $100.00 (+1378.02%)
- 確定: 6833件 (Win 1980 / Loss 2195 / Flat 2658) / skip 7708件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,478.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4421件 (Win 1185 / Loss 983 / Flat 2253) / skip 6970件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0360 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6140件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T17:11:07.133617+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78098.2
- Funnel: target 1088 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +18.24% | $6,734,853.77 |
| BEAMX/USDT:USDT | +5.39% | $2,525,527.57 |
| IDOL/USDT:USDT | +3.10% | $8,330,585.74 |
| EVAA/USDT:USDT | +2.77% | $9,295,108.01 |
| JCT/USDT:USDT | +1.86% | $2,775,513.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.84% | +3.86% |
| EVAA/USDT:USDT | below_1h_threshold | +2.34% | +2.35% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.51% | +1.52% |
| JASMY/USDT:USDT | below_1h_threshold | +0.97% | +0.99% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.97% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
