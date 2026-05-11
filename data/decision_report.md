# Decision Report

- generated_at: 2026-05-11T18:33:21.471411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4060**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4060, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.24% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.17% | **+1.00%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.77% | **+0.83%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.94% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 403件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T18:33:13.412673+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=82077.7
- Funnel: target 758 → liquid 193 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 84.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +16.98% | $28,557,026.17 |
| USELESS/USDT:USDT | +14.38% | $1,544,718.54 |
| B/USDT:USDT | +13.14% | $30,360,323.86 |
| ASTEROID/USDT:USDT | +12.07% | $2,613,867.70 |
| PENGUIN/USDT:USDT | +9.83% | $2,209,070.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_relative_strength | +5.03% | +4.80% |
| USELESS/USDT:USDT | below_1h_threshold | +4.34% | +4.11% |
| BASED/USDT:USDT | below_1h_threshold | +3.92% | +3.69% |
| XNY/USDT:USDT | below_1h_threshold | +3.53% | +3.31% |
| VVV/USDT:USDT | below_1h_threshold | +3.47% | +3.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
