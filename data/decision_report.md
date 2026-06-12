# Decision Report

- generated_at: 2026-06-12T10:39:51.689352+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6501**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=6501, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.35% | **+0.86%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.28% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.21** / 初期 $100.00 (+67.21%)
- 確定: 1375件 (Win 376 / Loss 443 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $167.21

## 4. Latest Market Context

- 更新: 2026-06-12T10:39:46.516028+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63690.0
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1, 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +95.65% | $154,054,543.30 |
| ESPORTS/USDT:USDT | +72.20% | $43,649,345.68 |
| NAORIS/USDT:USDT | +43.33% | $4,475,650.80 |
| XPL/USDT:USDT | +33.72% | $11,442,949.40 |
| AIN/USDT:USDT | +32.21% | $1,084,100.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLFI/USDT:USDT | below_1h_threshold | +2.82% | +2.88% |
| STG/USDT:USDT | below_1h_threshold | +2.70% | +2.76% |
| AIN/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |
| SEI/USDT:USDT | below_1h_threshold | +1.22% | +1.28% |
| LAB/USDT:USDT | below_1h_threshold | +0.79% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
