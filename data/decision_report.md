# Decision Report

- generated_at: 2026-07-31T13:01:16.856328+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10004**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10004, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.21% | **+0.16%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.02% | **+0.02%** |
| LIMIT_BB3S | 6/18 | 33.3% | -0.01% | **-0.00%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +4.34% | **+1.09%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.32% | **+1.04%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 2992件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2137件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0526 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.21** / 初期 $100.00 (+11.21%)
- 確定: 836件 (Win 270 / Loss 330 / Flat 236) / pending 5件 / skip 635件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.21

## 6. Latest Market Context

- 更新: 2026-07-31T13:01:09.735813+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63737.2
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +73.03% | $13,804,310.58 |
| AXTISTOCK/USDT:USDT | +45.69% | $6,722,977.67 |
| GIGGLE/USDT:USDT | +30.75% | $10,563,580.12 |
| CAP/USDT:USDT | +22.47% | $7,045,229.30 |
| AMZU/USDT:USDT | +19.24% | $1,707,291.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXTISTOCK/USDT:USDT | below_1h_threshold | +3.42% | +3.41% |
| COTI/USDT:USDT | below_1h_threshold | +1.92% | +1.91% |
| BULLA/USDT:USDT | below_1h_threshold | +1.73% | +1.72% |
| GRVT/USDT:USDT | below_1h_threshold | +1.41% | +1.39% |
| USOIL/USDT:USDT | below_1h_threshold | +1.11% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
