# Decision Report

- generated_at: 2026-05-07T04:17:32.544787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3561**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3561, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.43% | **+0.41%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.04% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.08% | **+0.68%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.78% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$105.22** / 初期 $100.00 (+5.22%)
- 確定: 56件 (Win 19 / Loss 21 / Flat 16) / skip 66件
- 成長率目線: 平均log +0.000909 / 幾何平均 +0.091% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $105.22

## 4. Latest Market Context

- 更新: 2026-05-07T04:17:28.635879+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80872.9
- Funnel: target 769 → liquid 186 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.8 >= 65=1, 4h RSI 82.4 >= 65=1, 4h RSI 76.1 >= 65=1, 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +252.33% | $1,533,503.09 |
| B3/USDT:USDT | +105.65% | $8,368,537.29 |
| DOGS/USDT:USDT | +78.26% | $10,368,894.47 |
| PENGUIN/USDT:USDT | +59.75% | $1,233,214.92 |
| FHE/USDT:USDT | +40.41% | $16,313,830.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KSM/USDT:USDT | below_1h_threshold | +4.30% | +4.21% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.85% | +3.76% |
| VVV/USDT:USDT | below_1h_threshold | +2.33% | +2.24% |
| BILL/USDT:USDT | below_1h_threshold | +1.77% | +1.68% |
| STX/USDT:USDT | below_1h_threshold | +1.76% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
