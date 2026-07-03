# Decision Report

- generated_at: 2026-07-03T17:43:35.694159+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8180**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.93% / filled 20/20。**
- 全期間 MARKET基準: n=8180, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.66% | **+1.24%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.16% | **+0.08%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.07% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.07** / 初期 $100.00 (+189.07%)
- 確定: 2499件 (Win 769 / Loss 833 / Flat 897) / skip 2242件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $289.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 980件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T17:43:29.562571+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=62221.1
- Funnel: target 834 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +22.84% | $9,333,222.18 |
| VELVET/USDT:USDT | +9.00% | $28,050,361.08 |
| BASED/USDT:USDT | +6.28% | $9,184,553.38 |
| TLM/USDT:USDT | +5.58% | $17,259,146.28 |
| BSB/USDT:USDT | +5.00% | $3,073,057.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +3.74% | +3.52% |
| NOM/USDT:USDT | below_1h_threshold | +3.49% | +3.27% |
| NEX/USDT:USDT | below_1h_threshold | +3.48% | +3.26% |
| VELVET/USDT:USDT | below_1h_threshold | +3.41% | +3.19% |
| LUNC/USDT:USDT | below_1h_threshold | +2.83% | +2.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
