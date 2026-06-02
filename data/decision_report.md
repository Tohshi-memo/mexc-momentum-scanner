# Decision Report

- generated_at: 2026-06-02T14:57:08.261207+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5457**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5457, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +2.64% | **+0.70%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.92% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_5PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.01% | **+0.66%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.17%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.37** / 初期 $100.00 (+34.37%)
- 確定: 969件 (Win 229 / Loss 294 / Flat 446) / skip 1049件
- 成長率目線: 平均log +0.000305 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $134.37

## 4. Latest Market Context

- 更新: 2026-06-02T14:57:03.045259+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.00% price=68094.4
- Funnel: target 773 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +44.43% | $5,133,118.63 |
| USELESS/USDT:USDT | +30.45% | $4,290,517.23 |
| UB/USDT:USDT | +29.25% | $3,911,449.30 |
| MRVLSTOCK/USDT:USDT | +28.27% | $9,205,471.49 |
| RIF/USDT:USDT | +26.14% | $2,411,422.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.38% | +4.38% |
| UB/USDT:USDT | below_1h_threshold | +3.36% | +4.36% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.57% | +3.57% |
| RIF/USDT:USDT | below_1h_threshold | +1.43% | +2.44% |
| M/USDT:USDT | below_1h_threshold | +1.42% | +2.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
