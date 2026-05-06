# Decision Report

- generated_at: 2026-05-06T12:57:31.613409+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3458**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3458, expectancy=-0.15%
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
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.21% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.32% | **+1.39%** |
| MARKET_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.12% | **+1.06%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 10件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T12:57:28.364824+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=82246.5
- Funnel: target 770 → liquid 202 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +101.72% | $2,170,454.76 |
| BILL/USDT:USDT | +40.43% | $4,457,618.23 |
| FHE/USDT:USDT | +39.85% | $32,158,818.00 |
| IO/USDT:USDT | +35.20% | $14,273,110.72 |
| TONCOIN/USDT:USDT | +33.80% | $223,989,475.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.59% | +3.88% |
| DASH/USDT:USDT | below_1h_threshold | +3.51% | +3.80% |
| NOT/USDT:USDT | below_1h_threshold | +3.30% | +3.59% |
| FHE/USDT:USDT | below_1h_threshold | +2.71% | +3.00% |
| ENA/USDT:USDT | below_1h_threshold | +2.57% | +2.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
