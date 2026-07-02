# Decision Report

- generated_at: 2026-07-02T03:54:56.576329+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8044**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=8044, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |
| LIMIT_1PCT | 16/20 | 80.0% | -0.06% | **-0.05%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.42% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.07% | **+0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | -0.37% | **-0.09%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.23% | **-0.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.24% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.11** / 初期 $100.00 (+186.11%)
- 確定: 2441件 (Win 753 / Loss 814 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $286.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 545件 (Win 136 / Loss 131 / Flat 278) / skip 910件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T03:39:56.438669+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=60740.3
- Funnel: target 825 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +231.19% | $77,045,948.17 |
| TLM/USDT:USDT | +43.30% | $7,634,922.38 |
| RIF/USDT:USDT | +32.51% | $4,071,283.90 |
| SLX/USDT:USDT | +19.18% | $8,309,822.52 |
| LIT/USDT:USDT | +18.14% | $10,951,115.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAIKO/USDT:USDT | below_relative_strength | +5.12% | +4.54% |
| M/USDT:USDT | below_1h_threshold | +3.33% | +2.76% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.65% | +2.08% |
| TLM/USDT:USDT | below_1h_threshold | +1.97% | +1.39% |
| NEAR/USDT:USDT | below_1h_threshold | +1.59% | +1.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
