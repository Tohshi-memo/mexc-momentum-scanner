# Decision Report

- generated_at: 2026-05-06T12:42:39.635252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3455**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3455, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +1.88% | **+0.50%** |
| LIMIT_8PCT | 2/20 | 10.0% | +4.73% | **+0.47%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.19% | **+0.05%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.04% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.29% | **+1.64%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.27% | **+1.02%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.42% | **+0.99%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 7件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T12:42:35.997684+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=82275.7
- Funnel: target 770 → liquid 201 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 75.6 >= 65=1, 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +72.48% | $1,782,937.43 |
| FHE/USDT:USDT | +45.31% | $31,553,823.88 |
| BILL/USDT:USDT | +39.82% | $4,251,927.26 |
| IO/USDT:USDT | +39.20% | $14,017,996.94 |
| LAB/USDT:USDT | +38.62% | $126,798,221.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +3.34% | +3.59% |
| ENA/USDT:USDT | below_1h_threshold | +2.81% | +3.06% |
| DASH/USDT:USDT | below_1h_threshold | +1.66% | +1.91% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.56% | +1.82% |
| CLANKER/USDT:USDT | below_1h_threshold | +1.44% | +1.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
