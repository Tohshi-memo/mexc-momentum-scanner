# Decision Report

- generated_at: 2026-07-01T20:55:18.875978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8015**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=8015, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.74% | **+0.33%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.88% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$275.07** / 初期 $100.00 (+175.07%)
- 確定: 2412件 (Win 738 / Loss 800 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $275.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.21** / 初期 $100.00 (+7.21%)
- 確定: 532件 (Win 135 / Loss 125 / Flat 272) / skip 894件
- 成長率目線: 平均log +0.000131 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $107.21

## 5. Latest Market Context

- 更新: 2026-07-01T20:55:11.462708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=60093.5
- Funnel: target 825 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1, 4h RSI 67.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +73.97% | $2,463,986.97 |
| LIT/USDT:USDT | +16.79% | $5,838,437.31 |
| RIF/USDT:USDT | +12.47% | $2,892,157.23 |
| B/USDT:USDT | +10.68% | $1,018,324.18 |
| NOM/USDT:USDT | +9.72% | $4,859,633.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.44% | +4.28% |
| BASED/USDT:USDT | below_1h_threshold | +3.40% | +3.25% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.38% | +3.22% |
| BEAT/USDT:USDT | below_1h_threshold | +2.21% | +2.05% |
| BSB/USDT:USDT | below_1h_threshold | +1.63% | +1.47% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
