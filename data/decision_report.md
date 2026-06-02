# Decision Report

- generated_at: 2026-06-02T14:09:21.566430+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5454**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5454, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.94% | **+0.38%** |
| LIMIT_5PCT | 3/20 | 15.0% | +1.65% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.22% | **-0.12%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.57% | **-0.34%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.64% | **-0.45%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.29% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.34** / 初期 $100.00 (+32.34%)
- 確定: 966件 (Win 227 / Loss 294 / Flat 445) / skip 1049件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $132.34

## 4. Latest Market Context

- 更新: 2026-06-02T14:09:19.228317+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=68483.8
- Funnel: target 773 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +46.43% | $4,507,590.85 |
| USELESS/USDT:USDT | +35.24% | $3,641,058.01 |
| CLO/USDT:USDT | +31.07% | $1,293,361.65 |
| EPIC/USDT:USDT | +28.42% | $3,293,245.97 |
| MRVLSTOCK/USDT:USDT | +27.99% | $8,175,575.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +2.73% | +3.16% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.72% | +2.15% |
| US/USDT:USDT | below_1h_threshold | +1.53% | +1.97% |
| UB/USDT:USDT | below_1h_threshold | +1.16% | +1.59% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.07% | +1.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
