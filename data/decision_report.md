# Decision Report

- generated_at: 2026-08-03T14:41:39.129595+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10224**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10224, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.83% | **-2.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.07% | **+0.93%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.57% | **+0.77%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.42% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.30% | **+3.14%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +4.24% | **+2.76%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +5.39% | **+2.70%** |
| MARKET_LONG | 20/20 | 100.0% | +2.41% | **+2.41%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.05% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$576.35** / 初期 $100.00 (+476.35%)
- 確定: 3683件 (Win 1168 / Loss 1205 / Flat 1310) / skip 3102件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $576.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2352件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0263 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.67** / 初期 $100.00 (+15.67%)
- 確定: 1009件 (Win 324 / Loss 391 / Flat 294) / pending 6件 / skip 683件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000539 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.67

## 6. Latest Market Context

- 更新: 2026-08-03T14:41:24.122195+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.82% price=63834.2
- Funnel: target 929 → liquid 162 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.1 >= 65=1, 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +233.12% | $3,841,158.35 |
| BICO/USDT:USDT | +60.23% | $16,826,154.96 |
| 1000RATS/USDT:USDT | +34.35% | $38,271,449.73 |
| BTW/USDT:USDT | +26.44% | $6,539,679.96 |
| SKYAI/USDT:USDT | +25.93% | $5,573,478.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +4.46% | +3.65% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.29% | +3.48% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.22% | +3.41% |
| METASTOCK/USDT:USDT | below_1h_threshold | +4.16% | +3.35% |
| BTW/USDT:USDT | below_1h_threshold | +3.60% | +2.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
