# Decision Report

- generated_at: 2026-06-01T12:00:30.405539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5313**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=5313, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.22% | **+1.10%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.13% | **+0.74%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.36% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.10% | **+0.99%** |
| ASK_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.74% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 980件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T12:00:28.067551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=72565.7
- Funnel: target 776 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +140.06% | $36,891,560.15 |
| SLX/USDT:USDT | +105.75% | $8,023,280.18 |
| H/USDT:USDT | +89.03% | $34,024,061.57 |
| VIC/USDT:USDT | +62.27% | $1,201,007.71 |
| LAB/USDT:USDT | +60.63% | $227,762,113.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIC/USDT:USDT | below_1h_threshold | +0.93% | +0.76% |
| SIREN/USDT:USDT | below_1h_threshold | +0.88% | +0.72% |
| XPL/USDT:USDT | below_1h_threshold | +0.77% | +0.61% |
| H/USDT:USDT | below_1h_threshold | +0.67% | +0.51% |
| FHE/USDT:USDT | below_1h_threshold | +0.65% | +0.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
