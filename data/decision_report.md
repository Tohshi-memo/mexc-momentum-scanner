# Decision Report

- generated_at: 2026-06-07T20:02:18.228525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5997**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=5997, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.18% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.69% | **+5.69%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.41** / 初期 $100.00 (+50.41%)
- 確定: 1114件 (Win 270 / Loss 336 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $150.41

## 4. Latest Market Context

- 更新: 2026-06-07T20:02:15.578814+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=61268.2
- Funnel: target 768 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +21.08% | $3,306,569.77 |
| EPIC/USDT:USDT | +14.28% | $1,189,270.79 |
| BEAT/USDT:USDT | +11.50% | $55,696,257.97 |
| VELVET/USDT:USDT | +9.87% | $2,868,675.53 |
| BTW/USDT:USDT | +9.85% | $13,540,529.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +2.72% | +2.78% |
| VELVET/USDT:USDT | below_1h_threshold | +0.79% | +0.84% |
| BABY/USDT:USDT | below_1h_threshold | +0.78% | +0.84% |
| BEAT/USDT:USDT | below_1h_threshold | +0.74% | +0.80% |
| USOIL/USDT:USDT | below_1h_threshold | +0.52% | +0.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
