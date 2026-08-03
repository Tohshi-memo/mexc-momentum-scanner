# Decision Report

- generated_at: 2026-08-03T15:51:38.582591+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10230**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10230, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.40% | **+0.30%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.01% | **+2.71%** |
| MARKET_LONG | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.20% | **+1.92%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.94% | **+0.77%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +0.36% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$575.19** / 初期 $100.00 (+475.19%)
- 確定: 3689件 (Win 1169 / Loss 1207 / Flat 1313) / skip 3102件
- 成長率目線: 平均log +0.000474 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $575.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2358件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0062 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.58** / 初期 $100.00 (+15.58%)
- 確定: 1013件 (Win 325 / Loss 393 / Flat 295) / pending 5件 / skip 685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000485 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.58

## 6. Latest Market Context

- 更新: 2026-08-03T15:51:25.737512+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63758.5
- Funnel: target 929 → liquid 163 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1, 4h RSI 67.9 >= 65=1, 4h RSI 77.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +240.27% | $4,605,636.59 |
| BICO/USDT:USDT | +47.02% | $18,996,472.59 |
| SKYAI/USDT:USDT | +32.33% | $7,428,401.72 |
| 1000RATS/USDT:USDT | +31.01% | $38,747,171.81 |
| BTW/USDT:USDT | +27.88% | $6,542,003.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.01% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +4.01% | +4.28% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.38% | +3.65% |
| ADA/USDT:USDT | below_1h_threshold | +2.69% | +2.95% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.32% | +2.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
