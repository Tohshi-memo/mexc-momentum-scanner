# Decision Report

- generated_at: 2026-07-19T15:06:24.396416+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9050**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=9050, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.15% | **+1.45%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.04% | **+1.51%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.59% | **+1.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.66% | **+0.66%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.87% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.32** / 初期 $100.00 (+301.32%)
- 確定: 3112件 (Win 977 / Loss 993 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $401.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.59** / 初期 $100.00 (+27.59%)
- 確定: 1011件 (Win 262 / Loss 213 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0901 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $127.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.01** / 初期 $100.00 (+1.01%)
- 確定: 250件 (Win 86 / Loss 124 / Flat 40) / pending 5件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000426 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.01

## 6. Latest Market Context

- 更新: 2026-07-19T15:06:16.400776+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64531.9
- Funnel: target 885 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +123.01% | $47,971,879.30 |
| TLM/USDT:USDT | +93.88% | $9,389,798.81 |
| B/USDT:USDT | +50.67% | $32,177,952.55 |
| TAG/USDT:USDT | +23.51% | $4,934,196.54 |
| PI/USDT:USDT | +16.29% | $4,871,167.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +2.74% | +2.78% |
| PI/USDT:USDT | below_1h_threshold | +1.51% | +1.56% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.35% | +1.40% |
| BILL/USDT:USDT | below_1h_threshold | +1.33% | +1.37% |
| BLESS/USDT:USDT | below_1h_threshold | +1.24% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
