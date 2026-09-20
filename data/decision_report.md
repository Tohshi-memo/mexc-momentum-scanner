# Decision Report

- generated_at: 2026-09-20T12:11:19.347256+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15182**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15182, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.24% | **+0.49%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618 | 6/20 | 30.0% | -0.49% | **-0.15%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.20% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.55% | **+2.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.38% | **+1.55%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.41% | **+1.34%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.97% | **+1.23%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.40** / 初期 $100.00 (+1097.40%)
- 確定: 5708件 (Win 1705 / Loss 1841 / Flat 2162) / skip 6035件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3285件 (Win 910 / Loss 764 / Flat 1611) / skip 5308件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0254 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3675件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T12:11:08.428929+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80455.9
- Funnel: target 1050 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +64.81% | $7,411,646.43 |
| ONE/USDT:USDT | +34.98% | $53,656,710.46 |
| OFC/USDT:USDT | +25.93% | $2,495,908.64 |
| PIEVERSE/USDT:USDT | +21.47% | $1,245,960.22 |
| 4STOCK/USDT:USDT | +18.96% | $1,024,784.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.79% | +2.78% |
| BANK/USDT:USDT | below_1h_threshold | +1.56% | +1.55% |
| VVV/USDT:USDT | below_1h_threshold | +1.47% | +1.46% |
| INJ/USDT:USDT | below_1h_threshold | +1.05% | +1.04% |
| ALGO/USDT:USDT | below_1h_threshold | +0.92% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
