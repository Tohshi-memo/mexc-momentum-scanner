# Decision Report

- generated_at: 2026-11-01T20:26:14.271675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17994**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17994, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +5.77% | **+2.02%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.93% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.31% | **+1.96%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.60% | **+1.82%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.57% | **+1.67%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +6.13% | **+1.53%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,528.63** / 初期 $100.00 (+1428.63%)
- 確定: 6847件 (Win 1987 / Loss 2199 / Flat 2661) / skip 7708件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,528.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$378.75** / 初期 $100.00 (+278.75%)
- 確定: 4435件 (Win 1191 / Loss 986 / Flat 2258) / skip 6970件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0834 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $378.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T20:26:05.805576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77715.6
- Funnel: target 1088 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +32.27% | $8,879,727.84 |
| LYN/USDT:USDT | +20.14% | $1,090,057.19 |
| IDOL/USDT:USDT | +17.91% | $9,991,037.62 |
| BEAMX/USDT:USDT | +15.04% | $3,001,312.58 |
| Q/USDT:USDT | +11.77% | $4,288,629.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RT/USDT:USDT | below_1h_threshold | +4.16% | +4.23% |
| LSK/USDT:USDT | below_1h_threshold | +1.91% | +1.98% |
| BEAMX/USDT:USDT | below_1h_threshold | +1.83% | +1.90% |
| Q/USDT:USDT | below_1h_threshold | +1.24% | +1.31% |
| QNT/USDT:USDT | below_1h_threshold | +0.67% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
