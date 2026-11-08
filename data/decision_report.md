# Decision Report

- generated_at: 2026-11-08T10:06:13.858334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18431**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18431, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.37% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +5.30% | **+5.30%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.66% | **+1.46%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,641.35** / 初期 $100.00 (+1541.35%)
- 確定: 7126件 (Win 2051 / Loss 2274 / Flat 2801) / skip 7866件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,641.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7087件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1062 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6594件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000373 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T10:06:03.195099+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75857.4
- Funnel: target 1089 → liquid 101 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +281.16% | $12,105,818.57 |
| JCT/USDT:USDT | +59.95% | $4,007,597.58 |
| KOMA/USDT:USDT | +31.03% | $1,244,876.09 |
| AIOT/USDT:USDT | +14.82% | $2,850,878.97 |
| ICNT/USDT:USDT | +8.56% | $4,292,801.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +1.74% | +1.79% |
| JCT/USDT:USDT | below_1h_threshold | +1.19% | +1.24% |
| ICNT/USDT:USDT | below_1h_threshold | +1.08% | +1.14% |
| SOXL/USDT:USDT | below_1h_threshold | +0.82% | +0.88% |
| PEPE/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
