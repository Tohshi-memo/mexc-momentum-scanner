# Decision Report

- generated_at: 2026-06-17T23:51:33.619475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6976**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=6976, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.23% | **+0.18%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.23% | **+0.08%** |
| LIMIT_10PCT | 5/20 | 25.0% | -0.22% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.15% | **+0.11%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.15% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$201.69** / 初期 $100.00 (+101.69%)
- 確定: 1823件 (Win 498 / Loss 574 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $201.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.59** / 初期 $100.00 (+3.59%)
- 確定: 249件 (Win 66 / Loss 63 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000142 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0704 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $103.59

## 5. Latest Market Context

- 更新: 2026-06-17T23:51:24.457243+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=64459.2
- Funnel: target 790 → liquid 175 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +105.53% | $20,792,565.92 |
| O/USDT:USDT | +83.66% | $1,449,020.26 |
| SYN/USDT:USDT | +44.45% | $4,201,397.99 |
| RE/USDT:USDT | +16.07% | $1,828,080.26 |
| MITO/USDT:USDT | +13.74% | $1,661,815.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.51% | +3.21% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.79% | +2.49% |
| ENA/USDT:USDT | below_1h_threshold | +2.62% | +2.32% |
| UP/USDT:USDT | below_1h_threshold | +2.24% | +1.94% |
| WLFI/USDT:USDT | below_1h_threshold | +1.80% | +1.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
