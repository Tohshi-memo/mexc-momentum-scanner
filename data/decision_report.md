# Decision Report

- generated_at: 2026-07-19T15:11:17.235159+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9051**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=9051, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.32% | **+1.12%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.51% | **+1.05%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.66% | **+0.66%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.32** / 初期 $100.00 (+299.32%)
- 確定: 3113件 (Win 977 / Loss 994 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $399.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.14** / 初期 $100.00 (+27.14%)
- 確定: 1012件 (Win 262 / Loss 214 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0722 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定: 251件 (Win 86 / Loss 125 / Flat 40) / pending 4件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.83

## 6. Latest Market Context

- 更新: 2026-07-19T15:11:09.541561+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64527.0
- Funnel: target 885 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +115.79% | $49,074,912.45 |
| TLM/USDT:USDT | +84.59% | $9,515,851.46 |
| B/USDT:USDT | +46.85% | $32,500,912.64 |
| TAG/USDT:USDT | +25.18% | $4,949,318.72 |
| PI/USDT:USDT | +16.95% | $4,973,979.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.23% | +3.29% |
| TLM/USDT:USDT | below_1h_threshold | +2.73% | +2.79% |
| KAITO/USDT:USDT | below_1h_threshold | +2.34% | +2.39% |
| PI/USDT:USDT | below_1h_threshold | +1.92% | +1.97% |
| TAG/USDT:USDT | below_1h_threshold | +1.53% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
