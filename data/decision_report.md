# Decision Report

- generated_at: 2026-08-03T23:16:25.301610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10256, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.58% | **+0.06%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.28% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.79% | **+1.17%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.77%** |
| MARKET_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$592.88** / 初期 $100.00 (+492.88%)
- 確定: 3714件 (Win 1177 / Loss 1214 / Flat 1323) / skip 3103件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $592.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2384件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0653 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.86** / 初期 $100.00 (+16.86%)
- 確定: 1030件 (Win 332 / Loss 398 / Flat 300) / pending 5件 / skip 694件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000521 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.13% 残高後 $116.86

## 6. Latest Market Context

- 更新: 2026-08-03T23:16:19.039565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63539.9
- Funnel: target 929 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +15.22% | $6,050,055.58 |
| PLTRSTOCK/USDT:USDT | +14.63% | $3,314,439.60 |
| KORU/USDT:USDT | +11.75% | $16,943,138.05 |
| KOMA/USDT:USDT | +10.84% | $2,257,900.92 |
| ON/USDT:USDT | +9.86% | $2,717,290.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +2.09% |
| BEAT/USDT:USDT | below_1h_threshold | +1.88% | +1.96% |
| BANK/USDT:USDT | below_1h_threshold | +1.81% | +1.88% |
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.55% |
| AKT/USDT:USDT | below_1h_threshold | +1.45% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
