# Decision Report

- generated_at: 2026-08-22T02:56:45.001670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12299**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12299, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.70% | **+5.70%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.53% | **+2.27%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.12% | **+2.03%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.66% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.91** / 初期 $100.00 (+604.91%)
- 確定: 4417件 (Win 1353 / Loss 1442 / Flat 1622) / skip 4443件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $704.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.09** / 初期 $100.00 (+56.09%)
- 確定: 1905件 (Win 525 / Loss 455 / Flat 925) / skip 3805件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2707 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $156.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.59** / 初期 $100.00 (+18.59%)
- 確定: 1847件 (Win 548 / Loss 696 / Flat 603) / pending 6件 / skip 1927件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000616 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $118.59

## 6. Latest Market Context

- 更新: 2026-08-22T02:56:32.539745+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.79% price=78422.3
- Funnel: target 1018 → liquid 220 → pre 50 → checked 50 → surge 8 → strict 0
- Surge前reject: below_1h_threshold=40, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.8 >= 65=2, 4h RSI 96.9 >= 65=1, 4h RSI 81.1 >= 65=1, 4h RSI 75.2 >= 65=1, 4h RSI 69.6 >= 65=1, 4h RSI 95.9 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +287.21% | $3,981,927.48 |
| CATE/USDT:USDT | +78.11% | $12,293,841.87 |
| DASH/USDT:USDT | +33.39% | $12,756,067.35 |
| TRB/USDT:USDT | +31.16% | $5,359,043.11 |
| AGI/USDT:USDT | +30.35% | $1,788,778.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SUI/USDT:USDT | below_relative_strength | +5.42% | +4.63% |
| XRP/USDT:USDT | below_relative_strength | +5.04% | +4.25% |
| GALA/USDT:USDT | below_1h_threshold | +4.71% | +3.92% |
| CC/USDT:USDT | below_1h_threshold | +4.64% | +3.85% |
| ADA/USDT:USDT | below_1h_threshold | +4.61% | +3.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
