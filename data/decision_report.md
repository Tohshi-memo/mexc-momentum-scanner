# Decision Report

- generated_at: 2026-05-21T13:59:01.067510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4632**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4632, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.49% | **+0.25%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.18% | **+0.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 647件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T13:58:55.411724+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=77023.5
- Funnel: target 766 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +43.60% | $1,385,431.42 |
| EDEN/USDT:USDT | +41.70% | $33,668,522.49 |
| PROVE/USDT:USDT | +39.16% | $6,435,076.42 |
| ROAM/USDT:USDT | +38.08% | $2,313,346.34 |
| FIDA/USDT:USDT | +35.79% | $14,559,159.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.79% | +5.08% |
| ROAM/USDT:USDT | below_1h_threshold | +4.60% | +4.89% |
| LIT/USDT:USDT | below_1h_threshold | +3.83% | +4.11% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.56% | +3.84% |
| HYPE/USDT:USDT | below_1h_threshold | +3.00% | +3.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
