# Decision Report

- generated_at: 2026-06-07T16:34:50.097476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5980**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5980, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.71% | **-2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.99% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.51% | **+2.63%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.06% | **+2.43%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.80% | **+1.92%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.77% | **+1.88%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.70% | **+1.66%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.69** / 初期 $100.00 (+50.69%)
- 確定: 1097件 (Win 266 / Loss 329 / Flat 502) / skip 1444件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $150.69

## 4. Latest Market Context

- 更新: 2026-06-07T16:34:43.417369+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=62236.7
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 91.6 >= 65=1, 4h RSI 80.9 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +25.10% | $1,284,408.43 |
| VELVET/USDT:USDT | +10.60% | $2,354,455.89 |
| ESPORTS/USDT:USDT | +8.87% | $3,407,369.09 |
| H/USDT:USDT | +6.57% | $10,369,396.55 |
| SKYAI/USDT:USDT | +6.53% | $45,800,938.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.00% | +3.73% |
| BSB/USDT:USDT | below_1h_threshold | +3.93% | +3.66% |
| BEAT/USDT:USDT | below_1h_threshold | +3.54% | +3.28% |
| NEAR/USDT:USDT | below_1h_threshold | +3.41% | +3.15% |
| RAVE/USDT:USDT | below_1h_threshold | +3.33% | +3.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
