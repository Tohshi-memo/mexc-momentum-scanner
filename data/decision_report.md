# Decision Report

- generated_at: 2026-06-17T14:53:04.867560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6951**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=6951, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +4.18% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.71% | **+0.61%** |
| ASK_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.68% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1699件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定: 224件 (Win 57 / Loss 52 / Flat 115) / skip 138件
- 成長率目線: 平均log +0.000117 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0786 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $102.65

## 5. Latest Market Context

- 更新: 2026-06-17T14:52:58.001634+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=65092.5
- Funnel: target 790 → liquid 167 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +98.48% | $5,113,312.74 |
| ESPORTS/USDT:USDT | +46.95% | $12,880,305.74 |
| TAC/USDT:USDT | +41.44% | $1,167,526.60 |
| MAGMA/USDT:USDT | +32.31% | $1,019,234.30 |
| BLESS/USDT:USDT | +27.86% | $17,524,875.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARMSTOCK/USDT:USDT | below_1h_threshold | +3.99% | +4.21% |
| TAC/USDT:USDT | below_1h_threshold | +3.80% | +4.03% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.21% | +3.43% |
| ASTER/USDT:USDT | below_1h_threshold | +2.97% | +3.20% |
| AGT/USDT:USDT | below_1h_threshold | +2.95% | +3.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
