# Decision Report

- generated_at: 2026-06-09T05:44:58.587386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6118**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6118, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.43% | **+2.43%** |
| ASK_LONG | 20/20 | 100.0% | +2.06% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.62% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 10件 (TP 1 / SL 8 / EXP 1)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.01** / 初期 $100.00 (+55.01%)
- 確定: 1158件 (Win 289 / Loss 355 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $155.01

## 4. Latest Market Context

- 更新: 2026-06-09T05:44:55.317713+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=63355.6
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +40.67% | $24,608,677.59 |
| ZEST/USDT:USDT | +24.73% | $1,187,281.41 |
| SLX/USDT:USDT | +17.03% | $1,356,277.92 |
| CTR/USDT:USDT | +14.36% | $1,172,578.75 |
| POWER/USDT:USDT | +14.02% | $1,305,815.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.47% | +3.25% |
| CTR/USDT:USDT | below_1h_threshold | +3.21% | +2.99% |
| ZEST/USDT:USDT | below_1h_threshold | +2.78% | +2.56% |
| BANK/USDT:USDT | below_1h_threshold | +2.69% | +2.47% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.63% | +2.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
