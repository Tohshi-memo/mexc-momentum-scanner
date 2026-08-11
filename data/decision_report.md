# Decision Report

- generated_at: 2026-08-11T13:36:30.021713+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11263**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11263, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.52% | **+1.13%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.18% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 178件 (TP 68 / SL 105 / EXP 5)
- 最新: COOKIE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3937件 (Win 1230 / Loss 1285 / Flat 1422) / skip 3887件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.96** / 初期 $100.00 (+42.96%)
- 確定: 1519件 (Win 426 / Loss 361 / Flat 732) / skip 3155件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0429 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $142.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.64** / 初期 $100.00 (+14.64%)
- 確定: 1331件 (Win 407 / Loss 525 / Flat 399) / pending 0件 / skip 1403件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.64

## 6. Latest Market Context

- 更新: 2026-08-11T13:36:21.928678+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=64084.0
- Funnel: target 967 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +55.41% | $29,506,116.12 |
| BTR/USDT:USDT | +45.18% | $1,588,704.04 |
| TOAD/USDT:USDT | +40.91% | $1,585,574.81 |
| BLUAI/USDT:USDT | +36.89% | $20,949,990.88 |
| CYS/USDT:USDT | +27.03% | $23,401,129.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COOKIE/USDT:USDT | below_1h_threshold | +3.46% | +3.80% |
| UAI/USDT:USDT | below_1h_threshold | +2.49% | +2.83% |
| MMT/USDT:USDT | below_1h_threshold | +1.88% | +2.22% |
| SNXX/USDT:USDT | below_1h_threshold | +1.46% | +1.80% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.28% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
