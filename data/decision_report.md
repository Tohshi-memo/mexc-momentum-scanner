# Decision Report

- generated_at: 2026-05-07T02:32:43.164925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3533, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.47% | **-1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.78% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.71% | **+2.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.00% | **+1.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.71%** |
| MARKET_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定: 28件 (Win 9 / Loss 11 / Flat 8) / skip 66件
- 成長率目線: 平均log +0.000576 / 幾何平均 +0.058% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $101.63

## 4. Latest Market Context

- 更新: 2026-05-07T02:32:37.729480+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=80886.6
- Funnel: target 770 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1, 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +166.81% | $1,097,046.51 |
| DOGS/USDT:USDT | +65.98% | $7,547,486.18 |
| PENGUIN/USDT:USDT | +36.03% | $1,126,268.84 |
| FHE/USDT:USDT | +24.68% | $16,034,594.65 |
| LAB/USDT:USDT | +14.76% | $258,180,556.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.48% | +2.77% |
| LAB/USDT:USDT | below_1h_threshold | +2.47% | +2.75% |
| DOGS/USDT:USDT | below_1h_threshold | +2.42% | +2.71% |
| ORCA/USDT:USDT | below_1h_threshold | +2.00% | +2.29% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.37% | +1.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
