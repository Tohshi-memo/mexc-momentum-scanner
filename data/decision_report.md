# Decision Report

- generated_at: 2026-08-22T00:46:41.300179+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12280**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12280, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.74% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.91% | **+2.18%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.04% | **+1.84%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.77%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$678.93** / 初期 $100.00 (+578.93%)
- 確定: 4399件 (Win 1346 / Loss 1440 / Flat 1613) / skip 4442件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $678.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.96** / 初期 $100.00 (+54.96%)
- 確定: 1886件 (Win 520 / Loss 451 / Flat 915) / skip 3805件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1701 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.64** / 初期 $100.00 (+17.64%)
- 確定: 1830件 (Win 543 / Loss 694 / Flat 593) / pending 5件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000375 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $117.64

## 6. Latest Market Context

- 更新: 2026-08-22T00:46:29.084599+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.71% price=77756.2
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1, 4h RSI 95.2 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: funding_rate 75%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +243.91% | $3,435,538.77 |
| CATE/USDT:USDT | +71.31% | $11,910,654.85 |
| AGI/USDT:USDT | +29.73% | $1,639,021.12 |
| ENS/USDT:USDT | +19.69% | $2,959,967.17 |
| STX/USDT:USDT | +16.73% | $2,229,455.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.34% | +5.05% |
| KAITO/USDT:USDT | below_1h_threshold | +3.87% | +4.58% |
| DASH/USDT:USDT | below_1h_threshold | +3.23% | +3.93% |
| ETC/USDT:USDT | below_1h_threshold | +2.95% | +3.65% |
| STX/USDT:USDT | below_1h_threshold | +2.84% | +3.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
