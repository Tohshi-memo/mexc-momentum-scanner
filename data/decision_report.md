# Decision Report

- generated_at: 2026-07-19T15:01:16.042082+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9049**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=9049, expectancy=-0.01%
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
| LIMIT_2PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_5PCT | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

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

- 残高: **$399.33** / 初期 $100.00 (+299.33%)
- 確定: 3111件 (Win 976 / Loss 993 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $399.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.72** / 初期 $100.00 (+26.72%)
- 確定: 1010件 (Win 261 / Loss 213 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0818 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定: 249件 (Win 85 / Loss 124 / Flat 40) / pending 5件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.84

## 6. Latest Market Context

- 更新: 2026-07-19T15:01:08.369616+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64579.9
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +128.58% | $46,878,696.47 |
| TLM/USDT:USDT | +81.49% | $9,139,868.51 |
| B/USDT:USDT | +58.37% | $31,786,585.63 |
| TAG/USDT:USDT | +23.09% | $4,927,080.27 |
| ESPORTS/USDT:USDT | +14.75% | $61,199,521.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +1.86% | +1.83% |
| TLM/USDT:USDT | below_1h_threshold | +1.09% | +1.06% |
| BILL/USDT:USDT | below_1h_threshold | +0.91% | +0.88% |
| AKE/USDT:USDT | below_1h_threshold | +0.88% | +0.85% |
| HOME/USDT:USDT | below_1h_threshold | +0.87% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
