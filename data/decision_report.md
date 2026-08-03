# Decision Report

- generated_at: 2026-08-03T19:46:31.863159+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10245, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.13% | **-2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_4PCT | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +4.93% | **+2.96%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.48% | **+2.24%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.68% | **+1.65%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.37% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$597.28** / 初期 $100.00 (+497.28%)
- 確定: 3703件 (Win 1175 / Loss 1210 / Flat 1318) / skip 3103件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $597.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2373件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.77** / 初期 $100.00 (+16.77%)
- 確定: 1023件 (Win 330 / Loss 396 / Flat 297) / pending 6件 / skip 691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000491 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NBISSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.77

## 6. Latest Market Context

- 更新: 2026-08-03T19:46:23.269121+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63920.1
- Funnel: target 929 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +27.76% | $2,497,867.53 |
| HOME/USDT:USDT | +11.86% | $3,163,960.77 |
| PIPPIN/USDT:USDT | +9.89% | $3,241,754.97 |
| SKYAI/USDT:USDT | +8.83% | $10,783,942.52 |
| SNXX/USDT:USDT | +7.55% | $7,086,608.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.28% | +3.14% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.00% |
| FET/USDT:USDT | below_1h_threshold | +1.91% | +1.77% |
| UAI/USDT:USDT | below_1h_threshold | +1.77% | +1.64% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.44% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
