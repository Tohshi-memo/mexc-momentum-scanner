# Decision Report

- generated_at: 2026-06-02T20:54:23.431141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5488**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5488, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.23% | **-2.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.66% | **+0.55%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.36% | **+3.36%** |
| MARKET_LONG | 20/20 | 100.0% | +3.18% | **+3.18%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.77%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.19% | **+1.57%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1073件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T20:54:20.074677+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=67513.8
- Funnel: target 770 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +34.96% | $13,631,076.47 |
| LAB/USDT:USDT | +20.31% | $190,297,673.56 |
| ESPORTS/USDT:USDT | +16.17% | $9,569,015.53 |
| LIT/USDT:USDT | +15.87% | $5,743,733.80 |
| GENIUS/USDT:USDT | +11.21% | $1,000,994.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PANWSTOCK/USDT:USDT | below_relative_strength | +5.31% | +4.97% |
| EDGE/USDT:USDT | below_relative_strength | +5.04% | +4.70% |
| LAB/USDT:USDT | below_1h_threshold | +4.74% | +4.40% |
| QNT/USDT:USDT | below_1h_threshold | +4.65% | +4.30% |
| BSB/USDT:USDT | below_1h_threshold | +4.64% | +4.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
