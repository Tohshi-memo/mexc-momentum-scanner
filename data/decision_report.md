# Decision Report

- generated_at: 2026-06-01T13:57:31.369055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5322**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=5322, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.60% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| ASK_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 989件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T13:57:25.908888+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.04% price=71445.4
- Funnel: target 776 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +105.89% | $39,417,675.78 |
| H/USDT:USDT | +105.51% | $42,028,187.86 |
| SLX/USDT:USDT | +68.07% | $9,217,398.62 |
| LAB/USDT:USDT | +65.45% | $234,887,194.82 |
| VIC/USDT:USDT | +47.30% | $1,467,137.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +4.62% | +5.66% |
| UKOIL/USDT:USDT | below_1h_threshold | +4.24% | +5.28% |
| STG/USDT:USDT | below_1h_threshold | +1.50% | +2.53% |
| NEX/USDT:USDT | below_1h_threshold | +1.49% | +2.52% |
| NVIDIA/USDT:USDT | below_1h_threshold | +1.40% | +2.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
