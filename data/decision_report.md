# Decision Report

- generated_at: 2026-05-06T12:52:27.285185+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3457**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3457, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.21% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.53% | **+1.64%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.12% | **+1.06%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 9件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T12:52:23.739375+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=82359.9
- Funnel: target 770 → liquid 201 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.7 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +91.25% | $2,055,985.03 |
| FHE/USDT:USDT | +41.88% | $32,016,776.23 |
| BILL/USDT:USDT | +40.04% | $4,412,823.70 |
| LAB/USDT:USDT | +38.87% | $127,911,561.61 |
| IO/USDT:USDT | +38.26% | $14,128,097.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.45% | +4.61% |
| TONCOIN/USDT:USDT | below_1h_threshold | +4.43% | +4.58% |
| ENA/USDT:USDT | below_1h_threshold | +3.51% | +3.66% |
| XPL/USDT:USDT | below_1h_threshold | +3.18% | +3.33% |
| DASH/USDT:USDT | below_1h_threshold | +3.13% | +3.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
