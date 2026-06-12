# Decision Report

- generated_at: 2026-06-12T05:19:32.055105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6464**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6464, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.12% | **+0.53%** |
| LIMIT_BB3S | 2/20 | 10.0% | +2.90% | **+0.29%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.53% | **+0.27%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.25% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.39% | **+2.39%** |
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.23% | **+1.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.66% | **+1.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$156.78** / 初期 $100.00 (+56.78%)
- 確定: 1339件 (Win 353 / Loss 430 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $156.78

## 4. Latest Market Context

- 更新: 2026-06-12T05:19:24.198846+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=63490.6
- Funnel: target 783 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +71.68% | $140,613,833.71 |
| H/USDT:USDT | +37.27% | $39,926,026.14 |
| XPL/USDT:USDT | +32.53% | $6,493,787.74 |
| NAORIS/USDT:USDT | +28.18% | $1,759,506.45 |
| SKYAI/USDT:USDT | +23.78% | $14,163,733.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.60% | +3.88% |
| BSB/USDT:USDT | below_1h_threshold | +2.39% | +2.67% |
| VELVET/USDT:USDT | below_1h_threshold | +1.98% | +2.27% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +2.04% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.61% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
