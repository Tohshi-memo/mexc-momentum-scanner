# Decision Report

- generated_at: 2026-08-03T19:51:26.006121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10246**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10246, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.53% | **-1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.15% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.25% | **+2.76%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.71% | **+2.04%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.91% | **+1.45%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$594.30** / 初期 $100.00 (+494.30%)
- 確定: 3704件 (Win 1175 / Loss 1211 / Flat 1318) / skip 3103件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $594.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2374件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0371 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1023件 (Win 330 / Loss 396 / Flat 297) / pending 6件 / skip 691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000465 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NBISSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-03T19:51:17.252629+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63915.2
- Funnel: target 929 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +20.05% | $2,587,138.34 |
| HOME/USDT:USDT | +12.46% | $3,171,711.55 |
| PIPPIN/USDT:USDT | +9.95% | $3,277,431.78 |
| SKYAI/USDT:USDT | +7.77% | $10,835,288.35 |
| SNXX/USDT:USDT | +7.25% | $7,159,724.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.83% | +3.71% |
| BEAT/USDT:USDT | below_1h_threshold | +2.96% | +2.84% |
| FET/USDT:USDT | below_1h_threshold | +2.61% | +2.49% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.01% |
| UAI/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
