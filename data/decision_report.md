# Decision Report

- generated_at: 2026-06-10T18:50:06.522413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6240**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6240, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.98% | **+1.98%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.79% | **+0.81%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.21% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.49** / 初期 $100.00 (+50.49%)
- 確定: 1231件 (Win 308 / Loss 384 / Flat 539) / skip 1570件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $150.49

## 4. Latest Market Context

- 更新: 2026-06-10T18:50:01.840500+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=61790.1
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1, 4h RSI 73.4 >= 65=1, 4h RSI 67.6 >= 65=1, 4h RSI 86.0 >= 65=1, 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +19.60% | $16,654,293.64 |
| FOLKS/USDT:USDT | +19.50% | $7,005,381.99 |
| POWER/USDT:USDT | +7.58% | $1,813,848.96 |
| ESPORTS/USDT:USDT | +7.56% | $25,464,135.71 |
| UAI/USDT:USDT | +5.93% | $1,974,596.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWER/USDT:USDT | below_1h_threshold | +2.86% | +3.10% |
| KAT/USDT:USDT | below_1h_threshold | +2.85% | +3.09% |
| JCT/USDT:USDT | below_1h_threshold | +2.52% | +2.76% |
| WLFI/USDT:USDT | below_1h_threshold | +1.46% | +1.71% |
| STG/USDT:USDT | below_1h_threshold | +1.43% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
