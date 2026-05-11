# Decision Report

- generated_at: 2026-05-11T14:58:00.255200+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4045**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4045, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.54% | **+3.54%** |
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.62% | **+1.29%** |
| ASK_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.84% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 388件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T14:57:53.966276+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=80858.4
- Funnel: target 762 → liquid 187 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1, 4h RSI 84.5 >= 65=1, 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +57.79% | $20,344,633.30 |
| TROLLSOL/USDT:USDT | +48.73% | $4,940,829.17 |
| SAGA/USDT:USDT | +37.95% | $4,386,748.84 |
| US/USDT:USDT | +31.11% | $14,989,491.68 |
| PENGUIN/USDT:USDT | +30.78% | $1,886,228.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.23% | +2.45% |
| ALCH/USDT:USDT | below_1h_threshold | +2.21% | +2.42% |
| NVIDIA/USDT:USDT | below_1h_threshold | +2.04% | +2.25% |
| PARTI/USDT:USDT | below_1h_threshold | +1.96% | +2.18% |
| KITE/USDT:USDT | below_1h_threshold | +1.93% | +2.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
