# Decision Report

- generated_at: 2026-06-12T04:34:38.136736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6456, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.78% | **+0.51%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.56% | **+0.17%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.94% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.69** / 初期 $100.00 (+53.69%)
- 確定: 1332件 (Win 348 / Loss 428 / Flat 556) / skip 1685件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $153.69

## 4. Latest Market Context

- 更新: 2026-06-12T04:34:32.482605+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=63719.1
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +93.27% | $137,635,127.31 |
| XPL/USDT:USDT | +32.47% | $5,663,254.71 |
| ESPORTS/USDT:USDT | +23.17% | $30,161,845.85 |
| NAORIS/USDT:USDT | +22.74% | $1,571,369.40 |
| H/USDT:USDT | +21.17% | $39,215,652.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.68% | +3.31% |
| H/USDT:USDT | below_1h_threshold | +3.23% | +2.87% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.92% | +2.56% |
| ORDI/USDT:USDT | below_1h_threshold | +2.44% | +2.08% |
| LAB/USDT:USDT | below_1h_threshold | +1.61% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
