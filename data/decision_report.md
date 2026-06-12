# Decision Report

- generated_at: 2026-06-12T11:42:11.717188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6505**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=6505, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/17 | 35.3% | +1.80% | **+0.64%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.58% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.87% | **+3.24%** |
| ASK_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.44% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.04** / 初期 $100.00 (+68.04%)
- 確定: 1378件 (Win 378 / Loss 444 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $168.04

## 4. Latest Market Context

- 更新: 2026-06-12T11:42:08.701126+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63758.2
- Funnel: target 774 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +93.54% | $156,108,944.93 |
| ESPORTS/USDT:USDT | +82.41% | $46,102,204.75 |
| NAORIS/USDT:USDT | +47.89% | $5,226,141.19 |
| XPL/USDT:USDT | +36.48% | $12,667,090.96 |
| SKYAI/USDT:USDT | +34.74% | $16,265,646.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_relative_strength | +5.05% | +4.91% |
| XMR/USDT:USDT | below_1h_threshold | +4.21% | +4.07% |
| COAI/USDT:USDT | below_1h_threshold | +4.11% | +3.96% |
| LAB/USDT:USDT | below_1h_threshold | +3.94% | +3.80% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.35% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
