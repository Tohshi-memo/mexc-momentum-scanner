# Decision Report

- generated_at: 2026-08-03T14:26:38.720775+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10220**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10220, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.75% | **+0.41%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.01% | **+2.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.08% | **+2.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.15% | **+2.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.04% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$571.98** / 初期 $100.00 (+471.98%)
- 確定: 3679件 (Win 1167 / Loss 1205 / Flat 1307) / skip 3102件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $571.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2348件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1005件 (Win 323 / Loss 391 / Flat 291) / pending 6件 / skip 683件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000527 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-03T14:26:24.333568+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=63449.9
- Funnel: target 929 → liquid 160 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.3 >= 65=1, 4h RSI 65.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +207.80% | $3,449,650.79 |
| BICO/USDT:USDT | +56.51% | $16,501,637.00 |
| 1000RATS/USDT:USDT | +28.30% | $37,882,333.77 |
| SKYAI/USDT:USDT | +26.10% | $5,277,379.58 |
| BTW/USDT:USDT | +23.67% | $6,426,496.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +4.46% | +4.25% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.36% | +4.16% |
| METASTOCK/USDT:USDT | below_1h_threshold | +4.16% | +3.95% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +3.18% | +2.97% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.65% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
