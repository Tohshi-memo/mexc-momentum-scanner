# Decision Report

- generated_at: 2026-06-03T13:58:30.607382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5548**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=5548, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.04% | **+0.36%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.19% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.29% | **+0.19%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.86** / 初期 $100.00 (+31.86%)
- 確定: 1002件 (Win 239 / Loss 311 / Flat 452) / skip 1107件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AMDSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $131.86

## 4. Latest Market Context

- 更新: 2026-06-03T13:58:25.560553+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=66795.1
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +43.17% | $1,435,450.74 |
| EPIC/USDT:USDT | +34.16% | $3,216,131.01 |
| CLO/USDT:USDT | +33.89% | $5,411,975.39 |
| ENA/USDT:USDT | +33.36% | $65,674,205.04 |
| LIT/USDT:USDT | +31.70% | $10,877,747.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.30% | +4.69% |
| ENA/USDT:USDT | below_1h_threshold | +4.27% | +4.65% |
| WLD/USDT:USDT | below_1h_threshold | +4.14% | +4.52% |
| GUA/USDT:USDT | below_1h_threshold | +4.09% | +4.48% |
| GENIUS/USDT:USDT | below_1h_threshold | +3.52% | +3.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
