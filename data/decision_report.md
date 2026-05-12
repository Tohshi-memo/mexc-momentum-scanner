# Decision Report

- generated_at: 2026-05-12T20:48:05.990945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4161**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4161, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_BB3S | 8/16 | 50.0% | +0.03% | **+0.01%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +7.04% | **+3.52%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.28% | **+1.15%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.56% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定: 297件 (Win 86 / Loss 102 / Flat 109) / skip 425件
- 成長率目線: 平均log +0.000646 / 幾何平均 +0.065% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $121.16

## 4. Latest Market Context

- 更新: 2026-05-12T20:48:01.905453+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=80606.5
- Funnel: target 758 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.2 >= 65=1, 4h RSI 82.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +31.52% | $55,489,230.25 |
| DYM/USDT:USDT | +13.45% | $2,109,489.77 |
| SATO/USDT:USDT | +12.14% | $1,122,380.99 |
| PEAQ/USDT:USDT | +11.56% | $2,014,957.75 |
| LAB/USDT:USDT | +11.42% | $136,484,221.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +3.41% | +3.64% |
| BILL/USDT:USDT | below_1h_threshold | +3.27% | +3.50% |
| SATO/USDT:USDT | below_1h_threshold | +3.11% | +3.35% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.27% | +2.50% |
| STX/USDT:USDT | below_1h_threshold | +1.97% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
