# Decision Report

- generated_at: 2026-05-06T11:52:29.774785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3448**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3448, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.31% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | +0.30% | **+0.04%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.10% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.04% | **-0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.21% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.92% | **+0.46%** |
| ASK_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.69% | **+0.27%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.32% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 1件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T11:52:26.216353+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=82504.6
- Funnel: target 770 → liquid 204 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1, 4h RSI n/a=1, 4h RSI 65.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +49.65% | $3,061,638.78 |
| IO/USDT:USDT | +39.54% | $13,346,909.55 |
| B3/USDT:USDT | +39.26% | $1,534,711.98 |
| ZEC/USDT:USDT | +34.29% | $771,631,252.03 |
| FHE/USDT:USDT | +33.79% | $30,018,069.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.70% | +3.38% |
| TAG/USDT:USDT | below_1h_threshold | +2.69% | +2.37% |
| NEAR/USDT:USDT | below_1h_threshold | +2.29% | +1.97% |
| ENA/USDT:USDT | below_1h_threshold | +1.94% | +1.62% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.68% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
