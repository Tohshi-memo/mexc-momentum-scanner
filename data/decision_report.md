# Decision Report

- generated_at: 2026-06-12T14:37:50.987786+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6517**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=6517, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.72% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.17** / 初期 $100.00 (+67.17%)
- 確定: 1390件 (Win 383 / Loss 451 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000370 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $167.17

## 4. Latest Market Context

- 更新: 2026-06-12T14:37:47.974746+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.77% price=63686.8
- Funnel: target 774 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +129.49% | $55,870,449.07 |
| VELVET/USDT:USDT | +82.67% | $163,510,215.95 |
| NAORIS/USDT:USDT | +44.12% | $6,540,345.64 |
| SKYAI/USDT:USDT | +38.83% | $17,737,994.44 |
| AIN/USDT:USDT | +38.78% | $1,375,616.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGE/USDT:USDT | below_relative_strength | +5.57% | +4.80% |
| MSTRSTOCK/USDT:USDT | below_relative_strength | +5.37% | +4.60% |
| ETHFI/USDT:USDT | below_1h_threshold | +4.30% | +3.54% |
| SOXL/USDT:USDT | below_1h_threshold | +3.51% | +2.74% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.07% | +2.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
