# Decision Report

- generated_at: 2026-10-25T15:11:14.265252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17431**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17431, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.06% | **+0.06%** |
| LIMIT_ATR | 5/20 | 25.0% | +0.16% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.29% | **+1.94%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.03% | **+1.93%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,575.16** / 初期 $100.00 (+1475.16%)
- 確定: 6684件 (Win 1946 / Loss 2130 / Flat 2608) / skip 7308件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXIS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,575.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.30** / 初期 $100.00 (+219.30%)
- 確定: 3974件 (Win 1104 / Loss 934 / Flat 1936) / skip 6868件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1885 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXIS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $319.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5589件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000591 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T15:11:04.846981+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80666.9
- Funnel: target 1070 → liquid 119 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +55.99% | $10,623,830.30 |
| CAP/USDT:USDT | +42.58% | $3,011,161.69 |
| T/USDT:USDT | +19.79% | $8,180,265.08 |
| SKYAI/USDT:USDT | +19.18% | $1,321,546.34 |
| USELESS/USDT:USDT | +14.07% | $5,267,172.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.37% | +2.31% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.76% | +1.70% |
| TAG/USDT:USDT | below_1h_threshold | +1.66% | +1.60% |
| CT/USDT:USDT | below_1h_threshold | +1.52% | +1.46% |
| ZRO/USDT:USDT | below_1h_threshold | +1.13% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
